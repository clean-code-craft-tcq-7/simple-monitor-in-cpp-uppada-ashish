#include <thread>
#include <chrono>
#include <iostream>

using std::cout, std::flush;
using std::this_thread::sleep_for;
using std::chrono::seconds;

int areVitalsOk(float temp, float pulse, float spo2) {
    return checkTemperature(temp) && checkPulseRate(pulse) && checkOxygenLevel(spo2);
}

int checkTemperature(float temp) {
    if (temp < 95 || temp > 102) {
        cout << "Temperature is critical!\n";
        blinkWarning();
        return 0;
    }
    return 1;
}

int checkPulseRate(float pulse) {
    if (pulse < 60 || pulse > 100) {
        cout << "  Pulse Rate is out of range!\n";
        blinkWarning();
        return 0;
    }
    return 1;
}

int checkOxygenLevel(float spo2) {
    if (spo2 < 90) {
        cout << " Oxygen Saturation is out of range!\n";
        blinkWarning();
        return 0;
    }
    return 1;
}

void blinkWarning() {
    for (int i = 0; i < 6; i++) {
        cout << "\r* " << flush;
        sleep_for(seconds(1));
        cout << "\r *" << flush;
        sleep_for(seconds(1));
    }
}
