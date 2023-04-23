$(document).ready(function () {
  $(".image-section").hide();
  $(".loader").hide();
  $("#result").hide();
  $("#probability").hide();

  function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $("#imagePreview").css(
          "background-image",
          "url(" + e.target.result + ")"
        );
        $("#imagePreview").hide();
        $("#imagePreview").fadeIn(400);
      };
      reader.readAsDataURL(input.files[0]);
    }
  }
  $("#imageUpload").change(function () {
    $(".image-section").show();
    $("#btn-predict").show();
    $("#result").text("");
    $("#probability").text("");
    $("#result").hide();
    $("#probability").hide();
    readURL(this);
  });

  $("#btn-predict").click(function () {
    var form_data = new FormData($("#upload-file")[0]);

    $(this).hide();
    $(".loader").show();

    $.ajax({
      type: "POST",
      url: "/predict",
      data: form_data,
      contentType: false,
      cache: false,
      processData: false,
      async: true,
      success: function (data) {
        $(".loader").hide();
        $("#result").fadeIn(300);
        $("#probability").fadeIn(300);
        $("#result").text(" Result:  " + data.predict);
        $("#probability").text(" Probability:  " + data.probability);
      },
    });
  });
});
