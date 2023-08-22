list=[1,2,3,4,5,6]

even=[i for i in list if i%2==0]
print("even no's:",even)
odd=[j for j in list if j%2!=0]
print("odd no's:",odd)

fruits=['apple','orange','banana','kiwi','grapes']
fruits_wt_a=[i for i in fruits if 'a' in i]
print(fruits_wt_a)
fruits_wot_a=[i for i in fruits if 'a' not in i]
print(fruits_wot_a)