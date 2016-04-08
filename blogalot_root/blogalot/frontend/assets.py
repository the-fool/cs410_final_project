from flask_assets import Environment, Bundle

css_blogalot = Bundle("scss/blogalot.scss",
                      filters="scss", output="css/blogalot.css",
                      debug=False)

css_all = Bundle(css_blogalot, filters="cssmin", output="css/blogalot.min.css")

