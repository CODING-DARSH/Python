
# # Global login state
# is_logged_in = False

# # Decorator
# def login_required(func):
#     def wrapper(*args, **kwargs):
#         if is_logged_in:
#             return func(*args, **kwargs)
#         else:
#             print("Access Denied. Please log in first.")
#     return wrapper

# # Functions with decorator
# @login_required
# def view_profile(user_id,name):
#     print("Profile details shown.")
#     print(f"{user_id} {name}")
#     return {"user_id":10,"name":name}

# @login_required
# def edit_profile():
#     print("Profile updated.")

# # -------------------
# # Test Cases
# # -------------------
# print("Case 1: Not logged in")
# view_profile()   # Should deny access
# edit_profile()   # Should deny access

# print("\nCase 2: After logging in")
# is_logged_in = True  # simulate login
# view_profile(10,"Darsh")   # Should show profile
# edit_profile()   # Should update profile




# def retry(func):
#     def value():



# @retry
# def unstable_function():
#     import random
#     if random.choice([True, False]):
#         raise ValueError("Random failure!")
#     return "Success!"
