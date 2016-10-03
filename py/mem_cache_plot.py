import matplotlib.pyplot as plt


def parse_results(path):
    def _retrieve_time(str_line):
        return float(str_line.split(":")[1].strip())

    simple = {}
    block = {}
    swapped = {}
    n = 0

    for line in open(path):
        if line.startswith("n ="):
            n = int(line[3:].strip())
        elif line.startswith("timeSimple"):
            simple[n] = _retrieve_time(line)
        elif line.startswith("timeBlock"):
            block[n] = _retrieve_time(line)
        elif line.startswith("timeSwapped"):
            swapped[n] = _retrieve_time(line)

    results = dict()
    results["Simple"] = simple
    results["Block"] = block
    results["Swapped"] = swapped
    return results


def generate_plot(data):
    ax = plt.figure(figsize=(20, 5)).add_subplot(111)
    for algo in data:
        keys = sorted(list(data[algo].keys()))
        values = [data[algo][key] for key in keys]
        ax.plot(keys, values)
        ax.legend([key for key in data], loc='upper left')

    first_key = next(iter(data.keys()))
    ticks = sorted(list(data[first_key].keys()))

    plt.tick_params(axis='both', labelsize=8)
    plt.xticks(ticks, rotation='vertical')
    plt.xlabel('n')
    plt.ylabel('time, s')
    plt.grid(True)
    return plt


def run(path_to_log_file):
    base_filename = path_to_log_file.split("/")[-1].split(".")[0]
    all_result = parse_results(path_to_log_file)
    generate_plot(all_result).savefig(base_filename + "-all.png", bbox_inches='tight')

    simple_result = {"Simple": all_result["Simple"]}
    generate_plot(simple_result).savefig(base_filename + "-simple.png", bbox_inches='tight')

    block_result = {"Block": all_result["Block"]}
    generate_plot(block_result).savefig(base_filename + "-block.png", bbox_inches='tight')

    swapped_result = {"Swapped": all_result["Swapped"]}
    generate_plot(swapped_result).savefig(base_filename + "-swapped.png", bbox_inches='tight')


linux_path1 = "/home/akasiyanik/Dev/fpmi/mem-cache-lab/logs/linux-1000-1100-float.log"
linux_path2 = "/home/akasiyanik/Dev/fpmi/mem-cache-lab/logs/linux-1000-1100-double.log"
linux_path3 = "/home/akasiyanik/Dev/fpmi/mem-cache-lab/logs/linux-1000-2000-float.log"
linux_path4 = "/home/akasiyanik/Dev/fpmi/mem-cache-lab/logs/linux-1000-2000-double.log"

mac_path1 = "/home/akasiyanik/Dev/fpmi/mem-cache-lab/logs/mac-1000-1100-float.log"
mac_path2 = "/home/akasiyanik/Dev/fpmi/mem-cache-lab/logs/mac-1000-2000-float.log"

run(linux_path1)
run(linux_path2)
run(linux_path3)
run(linux_path4)

