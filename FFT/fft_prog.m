close all
Fs = 3000;
L = 283280;
Xf = fft(AXg);
Yf = fft(AYg);
Zf = fft(AZg);
figure
plot(Fs/L*(-L/2:L/2-1),abs(Xf));
xlabel('f(Hz)');
ylabel('|fft(X)|');
xlim([-2000 2000])
grid on
figure
plot(Fs/L*(-L/2:L/2-1),abs(Yf));
xlabel('f(Hz)');
ylabel('|fft(Y)|');
xlim([-2000 2000])
grid on
figure
plot(Fs/L*(-L/2:L/2-1),abs(Zf));
xlabel('f(Hz)');
ylabel('|fft(Z)|');
xlim([-2000 2000])
grid on
