# -*- coding:utf-8 -*-


from pyecharts import Tree


data = [
    {
        "children": [
            {
                "children": [
                    {
                        "children": [
                			{
                				"children": [],
                				"name": "bug_report.md"
                			},
                			{
                				"children": [],
                				"name": "feature_request.md"
                			}
                		],
                		"name": "ISSUE_TEMPLATE"
                	}
                ],
                "name": ".github"
            },
            {
                "children": [
                    {
                        "children": [
                            {
                                "children": [],
                                "name": "README.md"
                            },
                            {
                            	"children": [],
                            	"name": "Redfoximg.jpg"
                            }
                        ],
                        "name": "image"
                    },
                    {
                        "children": [],
                        "name": "_config.yml"
                    },
                    {
                    	"children": [],
                    	"name": "README.md"
                    }
                ],
                "name": "docs"
            },
            {
                "children": [
                    {
                        "children": [
                        	{
                        		"children": [],
                        		"name": "__init__.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Bar.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Bar3D.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Boxplot.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Candlestick.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "EffectScatter.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Funnel.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Gauge.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Geo.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Geolines.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Graph.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Heatmap.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Kline.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Line.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Line3D.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Liquid.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Map.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Parallel.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Pie.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Polar.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Radar.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Sankey.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Scatter.py"
                        	},
                            {
                                "children": [],
                                "name": "Scatter3D.py"
                            },
                        	{
                        		"children": [],
                        		"name": "Surface3D.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Themerive.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Tree.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "TreeMap.py"
                        	},
                        	{
                        		"children": [],
                        		"name": "Wordcloud.py"
                        	},
                        ],
                        "name": "charts"
                    },
                    {
                    	"children": [],
                    	"name": "__init__.py"
                    },
                    {
                    	"children": [],
                    	"name": "_version.py"
                    },
                    {
                    	"children": [],
                    	"name": "defadd.py"
                    },
                    {
                    	"children": [],
                    	"name": "definfo.py"
                    }
                ],
                "name": "function"
            },
            {
            	"children": [],
            	"name": "__init__.py"
            },
            {
            	"children": [],
            	"name": "_config.yml"
            },
            {
            	"children": [],
            	"name": "LICENSE.txt"
            },
            {
            	"children": [],
            	"name": "README.md"
            },
            {
            	"children": [],
            	"name": "setup.py"
            }
        ],
        "name": "Redfox"
    }
]

tree = Tree("树图文件目录示例", width=1200, height=800)
tree.add("", data, tree_collapse_interval=2, tree_layout="radial")
tree.render("Redfox1.0.1bc文件目录树.html")
