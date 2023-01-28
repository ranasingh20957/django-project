function display()
{
    alert('WELCOME TO JS');
}

function addition()
{
    var a=parseInt(document.getElementById("t1").value)
    var b=parseInt(document.getElementById("t2").value)
    c=a+b;
    document.getElementById("result").innerHTML=c;
}