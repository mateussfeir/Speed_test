import speedtest

def test_speed():
    print('Collecting data, plese wait...')
    st = speedtest.Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    print(f"Download speed: {download_speed / 1024 / 1024:.2f} Mbps")
    print(f"Upload speed: {upload_speed / 1024 / 1024:.2f} Mbps")
    return (f'{download_speed / 1024 / 1024:.2f}'), (f'{upload_speed / 1024 / 1024:.2f}')


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
upload_data_list = []

while running:
    user_input = input('1) Test your internet speed.\n2) Print the internet speed results list.\n3) Calculate the average.\nq) Quit.\nChoose one of the options above: ')
    if user_input == '1':
        download_speed, upload_speed = test_speed()
        download_data_list.append(download_speed)
        upload_data_list.append(upload_speed)

    elif user_input == '2':
        print(f'Download list: {download_data_list}')
        print(f'Upload list: {upload_data_list}')

    elif user_input == '3':
        download_average = calculate_average(download_data_list)
        upload_average = calculate_average(upload_data_list)
        if len(download_data_list) > 0 and len(upload_data_list) > 0:
            print(f'Average download speed: {download_average:.2f} Mbps')
            print(f'Average upload speed: {upload_average:.2f} Mbps')
        else:
            continue
        
    elif user_input == 'q':
        running = False

    else:
        print('Sorry, you must choose 1 or q as input.')
print('User left.')
