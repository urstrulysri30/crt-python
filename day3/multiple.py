class photo:
    def candid(self):
        print("candid photos")


class slow_motion:
    def category(self):
        print("slow motion videos")


class reels:
    def category(self):
        print("instagram reels")


class video(slow_motion, reels):
    def candid(self):
        print('videos')


class nikon_z6(video, photo):
    pass


obj = nikon_z6()
obj.candid()
obj.category()
