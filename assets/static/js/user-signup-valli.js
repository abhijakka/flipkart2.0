function user_signup_valli() {
          var company_name = document.seller_signup_form.company_name;
          var own_name = document.seller_signup_form.own_name;
          var phone = document.seller_signup_form.phone;
          var email = document.seller_signup_form.email;
          var pancard = document.seller_signup_form.pancard;
          var logo= document.seller_signup_form.logo;
          var addressproof = document.seller_signup_form.addressproof;
          var address = document.seller_signup_form.address;  
          var password = document.seller_signup_form.password;
          var confirm_password = document.seller_signup_form.confirm_password;
          var letters = /^[A-Za-z  ]+$/;
          var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
          var letter = /[a-z]/;
          var upper = /[A-Z]/;
          var number = /[0-9]/;
          if (company_name.value.length <= 0) {
            alert(" company name is required");
            company_name.focus();
            return false;
          }
          if (company_name.value.length <= 2 || company_name.value.length > 20) {
            alert(" invalid company name ");
            company_name.focus();
            return false;
          }
          if (!company_name.value.match(letters)) {
            alert("Enter only alphabets at company name");
            company_name.focus();
            return false;
          }

          if (own_name.value.length <= 0) {
            alert("owner name is required");
            own_name.focus();
            return false;
          }
          if (own_name.value.length <= 2 || own_name.value.length > 20) {
            alert("invalid owner name ");
            own_name.focus();
            return false;
          }
          if (!own_name.value.match(letters)) {
            alert("Enter only alphabets at owner name");
            own_name.focus();
            return false;
          }
          if (phone.value.length <= 0) {
            alert("phone number is required");
            phone.focus();
            return false;
          }
          if (isNaN(phone.value)) {
            alert("Please enter digits for phonenumber");
            phone.focus();
            return false;
          }
          if (phone.value.length != 10) {
            alert("Phonenumber must contain 10 digits");
            phone.focus();
            return false;
          }   
          if (email.value.length <= 0) {
            alert("please enter gmail");
            email.focus();
            return false;
          }
        
          if (!email.value.match(mailformat)) {
            alert("invalid gmail");
            email.focus();
            return false;
          }
        
      
          if (pancard.value.length == "") {
            alert("please upload your pancard");
            pancard.focus();
            return false;
          }
          if (logo.value.length == "") {
            alert("please upload your companylogo");
            logo.focus();
            return false;
          }
          if (addressproof.value.length == "") {
            alert("please upload your addressproof");
            addressproof.focus();
            return false;
          }
          if (address.value.length <= 0) {
            alert("address is required");
            address.focus();
            return false;
          }
          if (password.value.length <= 0) {
            alert("Password cannot be blank");
            password.focus();
            return false;
          }
          if (!password.value.match(letter) ) {
            alert("password must contain one lowercase");
            password.focus();
            return false;
          }
          if (!password.value.match(upper)) {
            alert("password must contain one uppercase");
            password.focus();
            return false;
          }
          if (!password.value.match(number)) {
            alert("password must contain one number");
            password.focus();
            return false;
          }
          if (password.value.length != 6) {
            alert("Password must contain 6 characters");
            password.focus();
            return false;
          }
          if (confirm_password.value.length <= 0) {
            alert(" confirm Password cannot be blank");
            password.focus();
            return false;
          }
          if (password.value.length != confirm_password.value.length) {
            alert("Passwords must be equal ");
            confirm_password.focus();
            return false;
          }
          else{
             alert("registration successful...");
             return true;
          }
        



















}