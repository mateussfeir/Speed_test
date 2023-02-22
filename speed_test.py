import speedtest

def test_speed():
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    print(f"Download speed: {download_speed / 1024 / 1024:.2f} Mbps")
    print(f"Upload speed: {upload_speed / 1024 / 1024:.2f} Mbps")
    return (f'{download_speed / 1024 / 1024:.2f}')


def calculate_average(any_list):
    list_sum = 0
    for value in any_list:
        list_sum += float(value)
    if len(any_list) > 0:
        average = list_sum/len(any_list)
        return average
    else:  
        return None

running = True
download_data_list = []
upload_data = []

while running:
    user_input = input('1) Test your internet speed.\n2) Print the internet speed results list.\n3) Calculate the average.\nq) Quit.\nChoose one of the options above: ')
    if user_input == '1':
        download_speed = test_speed()
        download_data_list.append(download_speed)
    elif user_input == '2':
        print(download_data_list)
    elif user_input == '3':
        average = calculate_average(download_data_list)
        print(average)
    elif user_input == 'q':
        running = False
    else:
        print('Sorry, you must choose 1 or q as input.')
print('User left.')
