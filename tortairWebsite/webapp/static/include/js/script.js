
$(function () {
    var newDate = new Date()
        newDate.setDate(7 + (new Date().getDate()-1))
    var year = newDate.getFullYear();
    var month = newDate.getMonth()+1;
    var day =  newDate.getDate();
    var maxDate = year.toString()+'-'+month.toString()+'-'+day.toString();
    console.log(maxDate)

    $('#picker').datetimepicker({
        timepicker:false,
        datepicker: true,
        format: "Y-m-d",
        value: new Date(),
        minDate: new Date(),
        maxDate: new Date(maxDate)
    });
});
$('#toggle').on('click',function(){
    $('#picker').datetimepicker('toggle')
})
$( ".ok" ).on('click',function(){
    $("#myForm").submit();
});
$(document).ready(function(){
     $('.Mymodel').modal({backdrop: 'static', keyboard: false});
})










