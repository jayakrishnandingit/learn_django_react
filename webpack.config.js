var webpack = require("webpack");
const path = require('path');

module.exports = {
    entry: "./static/src/js/app.js",
    output: {
        path: path.resolve("./static/build/js"),
        filename: "app.bundle.js"
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: "babel-loader",
                query: {
                    presets: ["env", "react"]
                }
            },
            {
                test: /\.css$/,
                exclude: /node_modules/,
                loader: "style-loader!css-loader!autoprefixer-loader",
            },
            {
                test: /\.json$/,
                exclude: /node_modules/,
                loader: "json-loader"
            }
        ]
    }
}