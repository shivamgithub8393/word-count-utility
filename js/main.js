
// this function is for input text 
function submitData() {
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
    const url = "http://localhost:5001";

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
      $('#res_success').text("");
      $('#res_error').text("Something wrong happened");
    })
  }

  
}

// This function is for file input 
function submitFile() {
  $('#res_error').text("");
  $('#download_file').html("")
  $('#res_success').text("Please wait while file is being processed ...");

  let languageSelected = $("#floatingSelect").val()

  // check value is not empty
  var uploadedFile = $("#UploadFile")[0].files;
  console.log("length of file: " + uploadedFile.length)
  console.log("Uploaded File: " + uploadedFile)

  if(uploadedFile.length === 0) {
    $('#res_error').text("Please select file");
    $('#res_success').text("");
  }else{
    console.log("input file : ", uploadedFile[0], ' languageSelected', languageSelected);

    const url = "http://localhost:5001";
    var form_data = new FormData()
    form_data.append('language', languageSelected)
    form_data.append('uplodedFile', uploadedFile[0])

    $.ajax({
      type: "POST",
      url: url + "/word_count_file",
      contentType: false,
      cache: false,
      processData: false,
      // dataType: "json",
      // contentType: 'application/json;charset=UTF-8',
      // data: JSON.stringify({data: "hello"})
      data: form_data
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
      console.log("print Error ", err);
      $('#res_success').text("");
      $('#res_error').text("Something wrong happened");
    })
  }

  
}