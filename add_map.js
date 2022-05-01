// *** VIS 3 *** https://gist.github.com/michaschwab/411cbbd398e9b74e297f4aecf0410f70 
;(function() {

    var map;

    function Map(topology) {

        var geojson = topojson.feature(topology, topology.objects.towns),

            path = d3.geoPath().projection(null),

            svg3 = d3.select("#map")
                .append("svg")
                .attr('width', 615)
                .attr('height', 375),

            g = svg3.append("g").attr("class", "g-town"),

            town = g.selectAll("path.town").data(geojson.features)
                .enter().append("path")
                .attr("class", "town")
                .attr('d', path)
                .style('stroke', "white");
    }

    d3.json("data/ma-towns.topojson", function(err, topology) {
        map = new Map(topology)
    });

}());