import numpy
import matplotlib.pyplot as plt
import timeit
import  math

def read_file(file_to_read):
    read_signal = []

    for line in file_to_read:
        read_num = float(line)
        read_signal.append(read_num)

    file_to_read.close()
    return read_signal

def fourier(signal_to_trans):
    fft_signal = numpy.fft.fft(signal_to_trans)
    abs_fft = []
    fft_x = []

    for i in range(fft_signal.size):
        abs_num = abs(fft_signal[i])
        abs_fft.append(abs_num)
        coord_x = i / (fft_signal.size * 5 * 10 ** (-3))
        fft_x.append(coord_x)

    return abs_fft, fft_x

def plot_fft(signal_fft, freq, plot_name, fig):
    plt.figure(fig)
    plt.plot(freq, signal_fft)
    plt.title(plot_name)
    plt.xlabel('Freq, Hz')
    plt.xlim([0, 200])
    plt.ylim([0, 1000])
    plt.grid(True)
    #plt.show()

def process_signal(file,name,fig_num):
    signal = read_file(file)
    array = []
    for i in range(256):
        array.append(math.sin(2 * 3.14 * 10 / 255 * i))
    fourier_trans, x_axis = fourier(signal)
    plot_fft(fourier_trans, x_axis, name,fig_num)

