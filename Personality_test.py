from flask import Flask, render_template

personlity_test = Flask(__name__)


progress_bar = [('progress', 50)]

# @personlity_test.route("/")
# def homepage():
#     return render_template("homepage.html",
#                             pagetitle="Homepage",
#                             custom_css="homepage",
#                             page_head="Homepage",
#                             description="This is the Homepage")

@personlity_test.route("/") # free-personality-test
def personality_test():
    return render_template("testpage.html",
                            pagetitle="Myers-Briggs Personality Test",
                            custom_css="testpage",
                            page_head="Personality Test",
                            description="This is the Test Page",
                            progress=progress_bar,)

@personlity_test.route("/Test-results")
def types():
    return render_template("results.html",
                            pagetitle="Results Page",
                            custom_css="results",
                            page_head="Personality Types",
                            description="This is the Presonality Types Page")

if __name__ == "__main__":
    personlity_test.run()