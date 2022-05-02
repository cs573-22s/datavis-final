// *** VIS 3 *** https://gist.github.com/michaschwab/411cbbd398e9b74e297f4aecf0410f70 
;(function() {

    var map;

    var maptooltip = d3.select("body")
        .append("div")
        .attr("class", "mapToolTip")
        .style("position", "absolute")
        .style("display", "none")
        .style("min-width", "80px")
        .style("height", "auto")
        .style("background", "none repeat scroll 0 0 #ffffff")
        .style("border", "1px solid #414141")
        .style("padding", "14px")
        .style("text-align", "center");

    svg3 = d3.select("#map")
        .append("svg")
        .attr('width', 615)
        .attr('height', 375)

    function Map(topology) {

        var geojson = topojson.feature(topology, topology.objects.towns),

            path = d3.geoPath().projection(null),

            g = svg3.append("g").attr("class", "g-town"),
            
            //values = [...Array(351).keys()],

            town = g.selectAll("path.town").data(geojson.features)
                .enter().append("path")
                .attr("class", "town")
                .attr('d', path)
                .style('stroke', "white")
                .style('fill', "blue");

        d3.csv("data/town_percents.csv", function(data) {
            
            var color = d3.scaleLinear().domain([d3.min(data, function(d) { return +(d.percent); }),d3.max(data, function(d) { return +(d.percent); })])
                .range(["#85d1d4", "#164d66"])

            svg3.selectAll(".town")
                .data(data)
                .style("fill", function(d) {
                    return color(d['percent']);
                
                })
                .on("mousemove", function(d){
                    maptooltip
                    .style("left", d3.event.pageX - 50 + "px")
                    .style("top", d3.event.pageY - 70 + "px")
                    .style("display", "inline-block")
                    .html("Town: " + (d['town']) + "<br>" + "Percent Renter ELI: " + (Math.round(d['percent'] * 100) / 100 ));
                })
                .on("mouseout", function(d){ maptooltip.style("display", "none");});


            var defs = svg3.append("defs");
            var linearGradient = defs.append("linearGradient")
                .attr("id", "linear-gradient");

            linearGradient
                .attr("x1", "0%")
                .attr("y1", "0%")
                .attr("x2", "100%")
                .attr("y2", "0%");

            linearGradient.append("stop")
                .attr("offset", "0%")
                .attr("stop-color", "#85d1d4"); 

            linearGradient.append("stop")
                .attr("offset", "100%")
                .attr("stop-color", "#164d66");

            var rect_x = 0;
            var rect_y = 300;
            var min = d3.min(data, function(d) { return +(d.percent); })
            var max = d3.max(data, function(d) { return +(d.percent); })
            svg3.append("rect").attr("x",rect_x).attr("y",rect_y).attr("width", 300).attr("height", 20).style("fill", "url(#linear-gradient)");
            svg3.append("text").attr("x",rect_x).attr("y",rect_y+40).text((Math.round(min * 100) / 100 ));
            svg3.append("text").attr("x",rect_x+275).attr("y",rect_y+40).text((Math.round(max * 100) / 100 ));
            svg3.append("text").attr("x",rect_x/2).attr("y",rect_y-10).text("% Renter Households that are ELI").attr("font-size", 14);

        })

    }

    d3.json("data/ma-towns.topojson", function(err, topology) {
        map = new Map(topology)
    });
    


}());