from django.urls import path,include
from. import views


urlpatterns = [
     path('', views.home, name='home'),
      path('adminclick/', views.adminclick, name='adminclick'),
        path('studentclick/', views.studentclick, name='studentclick'),
      
      path('adminsignup/', views.adminsignup, name='adminsignup'),
      path('adminlogin/', views.admin_login, name='adminlogin'),
      path('logout/',views.user_logout,name='logout'),
            
      path('studentsignup/', views.studentsignup, name='studentsignup'),
      path('studentlogin/', views.student_login, name='studentlogin'),

      path('admindashboard/',views.admindashboard,name='admindashboard'),
      path('studentdashboard/',views.studentdashboard,name='studentdashboard'),

       path('add_book/', views.add_book, name='add_book'),
       path('list_students/', views.list_students, name='list_students'),
       path('view_books/', views.view_books, name='view_books'),
        path('view_books1/', views.view_books1, name='view_books1'),
        path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),

           path('profile/', views.profile, name='profile'),
            path('issue/', views.issue_book, name='issue_book'),
               path('view-issues/', views.view_issued_books, name='view_issued_books'),
  path('add_student/', views.add_student, name='add_student'),
     path('update_book/<int:book_id>/', views.update_book, name='update_book'),
   path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('pay_fine/<int:issue_id>/', views.pay_fine, name='pay_fine'),

path('update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('books/toggle/<int:book_id>/', views.toggle_book_status, name='toggle_book_status'),
    path('my-issued-books/', views.view_my_issued_books, name='view_my_issued_books'),
     path('students-returned-books/', views.students_who_returned_books, name='students_who_returned_books'),
    path('returned-books/', views.view_returned_books, name='view_returned_books'),
     path('request-book/', views.request_book, name='request_book'),
    path('view-book-requests/', views.view_book_requests, name='view_book_requests'),
    path('approve-request/<int:request_id>/', views.approve_request, name='approve_request'),
   path('approval_message/', views.approval_message, name='approval_message'),

      path('about/', views.about ,name='about'),
          path('add-to-cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
        path('order/download/<int:order_id>/', views.download_transaction_details, name='download_transaction_details'),

     path('transaction/<int:order_id>/', views.transaction_details, name='transaction_details'),

    path('sold-books/', views.view_sold_books, name='view_sold_books'),
          
]
