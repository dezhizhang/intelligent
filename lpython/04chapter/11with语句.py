try:
    print("code start")
    raise IndexError
except Exception as e:
    print(e)

finally:
    print("code end")





