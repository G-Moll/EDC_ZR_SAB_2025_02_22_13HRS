var content = document.getElementById("content" );
var endpoint = "https://jsonplaceholder.typicode.com/users";
var xhr = new XMLHttpRequest();
xhr.open( "GET", endpoint, true );
xhr.send();
xhr.addEventListener( "load", loadResponseData );

function loadResponseData( e ) {
    var htmlContent = "";
    var responseData = JSON.parse( e.target.responseText );
    for( var i = 0; i < responseData.length; i++ ) {
        htmlContent +=
        "<div class=card>" +
            "<h2>" + responseData[ i ].name + "</h2>" +
            "<h3>" + responseData[ i ].username +"</h3>" +
            "<p>" +
                "<strong>Phone</strong>" +
                "<span>" + responseData[ i ].phone + "</span>" +
            "</p>" +
        "</div>";
    }
    content.innerHTML = htmlContent;
}
