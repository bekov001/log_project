$("#count").click(function () {
    var value1 = parseFloat($("#1").val());
    var value2 = parseFloat($("#2").val());
    var value3 = parseFloat($("#3").val());
    let result = value1 * value2 * value3 / 1000000;
    $("#result").val(result);
    console.log(result)
})