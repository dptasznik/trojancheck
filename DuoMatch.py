class DuoMatch:

    def duo_match(filename, pass_msg):
        # open and read the file:
        f = open(filename, "r")
        f = f.read()

        lst = list(f.split())

        str = pass_msg

        for i in range(0, 10):
            if str[-1] == lst[i][0]:
                return lst[i]

        tkinter.messagebox.showwarning(message="Your codes did not work.")