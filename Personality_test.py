from flask import Flask, render_template

# identify the app's name and always use @app_name(@personality_test in our case) if you want to take actions inside the app
personlity_test = Flask(__name__)

# This is a sample progress bar to be represented in the answers page, you can comment it if you won't be using it
progress_bar = [('progress', 50)]

"""
- We use @personality_test.route() method to initiate a new page in our app
- At least one page is mandatory to be existed in the app, which is root page or homepage defined by "/"
- We use render_template() method to load an HTML page into our app, in this case we load "testpage.html" as the homepage
- render_template() method looks for the mentioned HTML page in a folder called "templates"(mandatory folder to be existed)
- The main attributes of the page has been declared here to be easily modified, and its code in the HTML file
- "pagetitle" attribute declares the page title to be shown in the page browser tab
- "custom_css" attribute looks for a css file called "testpage.css" in a path "/static/css/filename.css"
- The other attributes are declared in the same way, and its code in the HTML page
"""
@personlity_test.route("/")
def personality_test():
        return render_template("testpage.html",
                            pagetitle="Myers-Briggs Personality Test",
                            custom_css="testpage",
                            page_head="Personality Test",
                            description="This is the Test Page",
                            progress=progress_bar)

# Here we identify the 2nd page of our app
@personlity_test.route("/2nd-qs-page")
def second():
    return render_template("2nd-qs.html",
                            pagetitle="Myers-Briggs Personality Test",
                            custom_css="testpage",
                            page_head="Personality Test",
                            description="This is the Test Page")

# Here we identify the 3rd page of our app
@personlity_test.route("/3rd-qs-page")
def third():
    return render_template("3rd-qs.html",
                            pagetitle="Myers-Briggs Personality Test",
                            custom_css="testpage",
                            page_head="Personality Test",
                            description="This is the Test Page")

# Here we identify the 4th page of our app
@personlity_test.route("/4th-qs-page")
def fourth():
    return render_template("4th-qs.html",
                            pagetitle="Myers-Briggs Personality Test",
                            custom_css="testpage",
                            page_head="Personality Test",
                            description="This is the Test Page")

# Here we identify the 5th page of our app
@personlity_test.route("/5th-qs-page")
def fifth():
    return render_template("5th-qs.html",
                            pagetitle="Myers-Briggs Personality Test",
                            custom_css="testpage",
                            page_head="Personality Test",
                            description="This is the Test Page")

# Here we identify the 6th page of our app
@personlity_test.route("/Test-results")
def result():
    return render_template("results.html",
                            pagetitle="Results Page",
                            custom_css="results",
                            page_head="Personality Types",
                            description="This is the Presonality Types Page")

if __name__ == "__main__":
    personlity_test.run()
