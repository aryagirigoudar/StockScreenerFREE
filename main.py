# import multiprocessing as mp
# import os
# def load():
#     i=0
#     while i!=1000:
#         i+=1
#     print(i)

# def lo(p1):
#     i=0
#     print("started")
#     while check_pid(p1):
#         print(i)
#         i+=1

# def check_pid(pid):        
#     try:
#         os.kill(pid, 0)
#     except OSError:
#         return False
#     else:
#         return True


# if __name__ == "__main__":
#     mp.freeze_support()
#     mp.set_start_method('spawn')
#     # p2.start()
#     # p2.join()
#     p1 = mp.Process(target=load, )
#     p2 = mp.Process(target=lo(p1.pid))
#     p2.start()
#     p1.start()
#     p1.join()
    

    

# create.py  API = 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


import os

import openai

PROMPT = "An eco-friendly computer from the 90s in the style of vaporwave"

openai.api_key = os.getenv("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")

response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="256x256",
)

print(response["data"][0]["url"])