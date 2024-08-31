import subprocess

def line_notify(msg='PythonからLINE通知テスト！！！', token="UilkhmFzxCsLh7JiaptEEwWNy3LI2pD9fogNConcNxN"):
    subprocess.run(['curl', '-H', f'Authorization: Bearer {token}', '-F', f'message={msg}', 'https://notify-api.line.me/api/notify'])
