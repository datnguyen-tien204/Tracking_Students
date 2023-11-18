import subprocess

def run_streamlit_app():
    # Thay đổi đường dẫn đến tập tin .py của ứng dụng Streamlit của bạn
    streamlit_command = 'streamlit run main.py --server.port 8080'

    try:
        subprocess.run(streamlit_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_streamlit_app()
