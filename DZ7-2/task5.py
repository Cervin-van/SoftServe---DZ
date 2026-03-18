def reverse(st):
    lst = st.split(" ")
    lst = lst[::-1]
    return " ".join(lst)

print(reverse("hello world"))