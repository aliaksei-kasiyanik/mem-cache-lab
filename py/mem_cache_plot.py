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


result = parse_results("/Users/akasiyanik/FPMI/Толстиков/mem_cache/logs/test2.log")
plt1 = generate_plot(result)
plt1.savefig("from1000to1100.png")

result = parse_results("/Users/akasiyanik/FPMI/Толстиков/mem_cache/logs/test1.log")
plt2 = generate_plot(result)
plt2.savefig("from1000to2000.png")