function add_product() {
          var category = document.add_pro_form.category;
          var product_name = document.add_pro_form.product_name;
          var model_no = document.add_pro_form.model_no;
          var pro_prize = document.add_pro_form.pro_prize;
          var image = document.add_pro_form.image;
          var description= document.add_pro_form.description;
          if (category.value == "select") {
            alert("Category  is required...");
            category .focus();
            return false;
          }
          if (product_name.value.length <= 0) {
            alert(" product name cannot be empty");
            product_name.focus();
            return false;
          }
          if (product_name.value.length <= 2 ) {
            alert(" invalid product ");
            product_name.focus();
            return false;
          }
         if (model_no.value.length <= 0) {
            alert("model number cannot be empty");
            model_no.focus();
            return false;
          }
          if (pro_prize.value.length <= 0) {
            alert("product prize cannot be empty");
            pro_prize.focus();
            return false;
          }
          if (isNaN(pro_prize.value)) {
            alert("Please enter digits for prize");
            pro_prize.focus();
            return false;
          }
          if (image.value.length == "") {
            alert("please upload your product image");
            image.focus();
            return false;
          }
          if (description.value.length <= 0) {
            alert(" please write the Description");
            description.focus();
            return false;
          }
          else{
             alert("product added successfully...");
             return true;
          }


}