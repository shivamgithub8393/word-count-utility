

function submitSelected() {
  $('#res_error').text("");
  $('#download_file').html("")
  $('#res_success').text("Please wait while file is being processed ...");

  
  let input_data = $("#input_data").val().replace(/\n/g, " ")
  let languageSelected = $("#floatingSelect").val()

  // check value is not empty
  if(input_data === '') {
    $('#res_error').text("Text field can not be empty");
    $('#res_success').text("");
  }else{
    console.log("input data : ", input_data, ' languageSelected', languageSelected);
    const url = "http://localhost:5000";

    $.ajax({
      type: "GET",
      url: url + "/word_count?input_data=" + input_data+ '&language='+ languageSelected,
    }).done(function (res) {
      console.log("res ", res);
      if (res.status == "success") {
        console.log("print success");
        $('#res_success').text("Data Saved");
        $('#download_file').html("<a href='./output_files/output.xlsx' class='btn btn-danger' download>Download File</a>");
      } else {
        console.log("print Error");
        $('#res_error').text(res.data);
        $('#res_success').text("");
      }
    }).catch(err => {
      console.log("print Error");
        $('#res_error').text("Something wrong happened");
    })
  }

  
}