# def solution_8(x):
#     mu=3
#     eps = 0.0001
#     step=1
#     first = x
#     second = first+1/2
#
#     sumchan = 2
#     sumle = 1
#     biendemle = 3
#     biendemchan = 4
#     while(mu<20) :
#         first = second
#         if(step % 2 == 1):
#             second=first*(x**mu/mu)
#             mu = mu + 2
#         else:
#             sumle = sumle * biendemle
#             sumchan = sumchan * biendemchan
#
#             second=first+sumle/sumchan
#             biendemchan = biendemchan + 2
#             biendemle = biendemle + 2
#         step=step+1
#     return first
# print("solution 8 : ",solution_8(x))
# print("result 8 : ",math.asin(x))
