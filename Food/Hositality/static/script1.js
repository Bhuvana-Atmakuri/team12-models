 $( document ).ready(function() {
 $('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var k=id+2;
    var eml=this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:k
        },
        success:function(data){
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    });
});
});

