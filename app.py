import streamlit as st
import pandas as pd
import joblib

# meload model svm yang sudah dibuat, uncomment salah satu dari dua model yang sudah dibuat ini
# model = joblib.load("svm_model.pkl")
model = joblib.load("svm_model_ips_5.pkl")


# fungsi utama untuk menjalankan website
def main():
    st.title("Prediksi Kelulusan Mahasiswa Berdasarkan IPS dan IPK")

    # menambahkan elemen untuk input semua feature
    st.header("Masukkan parameter IPS 1-8 dan IPK")
    ips_1 = st.number_input("IPS 1", value=0.0, step=0.1, min_value=0.0, max_value=4.0)
    ips_2 = st.number_input("IPS 2", value=0.0, step=0.1, min_value=0.0, max_value=4.0)
    ips_3 = st.number_input("IPS 3", value=0.0, step=0.1, min_value=0.0, max_value=4.0)
    ips_4 = st.number_input("IPS 4", value=0.0, step=0.1, min_value=0.0, max_value=4.0)
    ips_5 = st.number_input("IPS 5", value=0.0, step=0.1, min_value=0.0, max_value=4.0)
    # ips_6 = st.number_input("IPS 6", step=0.1, min_value=0.0, max_value=4.0)
    # ips_7 = st.number_input("IPS 7", step=0.1, min_value=0.0, max_value=4.0)
    # ips_8 = st.number_input("IPS 8", step=0.1, min_value=0.0, max_value=4.0)
    ipk = st.number_input("IPK", value=0.0, step=0.1, min_value=0.0, max_value=4.0)

    # membuat dataframe dari user input
    try:
        input_data = {
            "IPS 1": [ips_1],
            "IPS 2": [ips_2],
            "IPS 3": [ips_3],
            "IPS 4": [ips_4],
            "IPS 5": [ips_5],
            # "IPS 6": [ips_6],
            # "IPS 7": [ips_7],
            # "IPS 8": [ips_8],
            "IPK ": [ipk],
        }

        shown_data = input_data

        input_df = pd.DataFrame(input_data)
        shown_df = pd.DataFrame(shown_data)

        # melakukan prediksi dengan menggunakan model
        prediction = model.predict(input_df)
    except:
        input_data = {
            "IPS 1": [ips_1],
            "IPS 2": [ips_2],
            "IPS 3": [ips_3],
            "IPS 4": [ips_4],
            "IPS 5": [ips_5],
            "IPK ": [ipk],
        }

        shown_data = {
            "IPS 1": [ips_1],
            "IPS 2": [ips_2],
            "IPS 3": [ips_3],
            "IPS 4": [ips_4],
            "IPS 5": [ips_5],
            # "IPS 6": [ips_6],
            # "IPS 7": [ips_7],
            # "IPS 8": [ips_8],
            "IPK ": [ipk],
        }

        input_df = pd.DataFrame(input_data)
        shown_df = pd.DataFrame(shown_data)

        # melakukan prediksi dengan menggunakan model
        prediction = model.predict(input_df)

    # tampilkan hasil prediksi setelah user menekan tombol
    if st.button("Prediksi Sekarang"):
        if (input_df == 0).all().all():
            st.error("Harap isi terlebih dahulu IPS dan IPK nya")
        else:
            with st.container():
                st.header("Hasil")
                st.write(
                    "Menampilkan hasil prediksi kelulusan untuk nilai berikut ini:"
                )
                st.write(shown_df)
                st.subheader("Hasil Prediksi:")
                if prediction[0] == 0:
                    st.success("Bisa lulus tepat waktu")
                else:
                    st.warning("Kemungkinan akan terlambat")


# fungsi untuk menjalankan aplikasi
if __name__ == "__main__":
    main()
