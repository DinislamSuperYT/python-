class android:
    name = None
    version = None
    google = None

    def __init_(self, name, version, google):
        pass

    def set_data(self, name, version, google):
        self.name = name
        self.version = version
        self.google = google

    def get_data(self):
        print(self.name, "version:", self.version, "google: ", self.google)

xiomi = android()
xiomi.name = "miui"
xiomi.version = 15
xiomi.google = True

huawei = android()
huawei.name = "MagicOS"
huawei.vrsion = 15
huawei.google = False

xiomi.get_data()
huawei.get_data()