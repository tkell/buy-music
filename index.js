var server = 'http://localhost:5000'

var getUrls = function() {
    var artist = $('#artist').val();
    var title = $('#title').val();
    var url = server + '/search?artist=' + artist + '&title=' + title;
    console.log(url)
    $.get(url, function(res) {
        for (var i=0; i< res.data.length; i++) {
            var link = res.data[i];
            var html = '<a href="' + link.url + '">' + link.site+ '</a><br />'
            $('#results-div').append(html)
        }
    });
}

