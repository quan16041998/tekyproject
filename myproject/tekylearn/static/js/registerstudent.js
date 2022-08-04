$(document).ready(function(){
   var v = $('#formregister').validate({
        rules: {
            'name': {
            required: true,
            minlength: 6,
            maxlength: 50,
            valid_name: true
          },
          'nameparent': {
            required: true,
            minlength: 6,
            maxlength: 50,
            valid_name: true
          },
          'email': {
            required: true,
            maxlength: 255,
            email: true,
            valid_email:true
          },
          'phonenumber': {
              required: true,
              digits: true,
              minlength: 9,
              maxlength: 11
          }
        },
        messages: {
            'name': {
            required: "Name can't be required",
            minlength: "Name must be more than or equal 6 letters",
            maxlength: "Name must be less than or equal 50 letters",
            
          },
          'email': {
            email: "Phai la email",
            maxlength: "Email must be less than or equal 255 letters",
          },
          'phone': {
              required: "Phone can't be required",
              digits: "Please type number only"
          }
        }
    })
    jQuery.validator.addMethod('valid_email', function (value) {
        var regex = /^[a-z0-9]+([-._][a-z0-9]+)*@([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{1,5}$/;
        return value.trim().match(regex);
      });
    jQuery.validator.addMethod('valid_phone', function (value) {
        var phone = $("#id_phonenumber").val()
        return 
      });

      $.validator.addMethod("valid_name", function (value) {
        var regex = /[a-z0-9._-]{3,15}$/ ;
        return value.trim().match(regex)
      },"Tên nhập vào không đúng");
    

    $('#id_name').blur(function(){
        v.element('#id_name'); 
       });

       $('#id_nameparent').blur(function(){
        v.element('#id_nameparent'); 
       });
       $('#id_email').blur(function(){
        v.element('#id_email'); 
       });
       $('#id_phonenumber').blur(function(){
        v.element('#id_phonenumber'); 
       });
});
