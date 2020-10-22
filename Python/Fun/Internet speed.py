import speedtest

# Speedtest solo funciona con python 2.7.0
# Opcion 3 no funciona correctamente

st=speedtest.Speedtest()
option=int(input("""What speed do you want to test:
1) Download Speed
2) Upload Speed
3) Ping
Your Choice"""))

if option==1:
    print(st.download(), "b/s")
elif option==2:
    print(st.upload(), "b/s")
elif option==3:
    servernames=[]
    st.get_servernames(servernames)
    print(st.results.ping, "b/s")
else:
    print("please enter the correct choice!")
