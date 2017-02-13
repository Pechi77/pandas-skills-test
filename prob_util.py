from IPython.display import Javascript, display
import ipywidgets as widgets

def create_js(df):
    js1 = "$.ajax({method: 'POST', contentType: 'application/json',"

    js2 = "data: JSON.stringify({})".format(df.to_json(orient='split'))

    js3 = """,url:"http://localhost:5000/post",
                success: function(result){
                    console.log('success!');
                    element.append(result['result']);
                    console.log(result);
                },
               error: function(result){
                   console.log(result)
               }
            });"""

    return js1 + js2 + js3

def button_maker(prob_num):
    button = widgets.Button(description="Check Problem {}".format(prob_num))
    
    def on_button_clicked(b):
        var = 'my_answer' + str(prob_num)
        if var in globals():
            js = create_js(my_answer1)
            display(Javascript(js))
        else:
            print('Variable {} has not been created'.format(var))
    
    button.on_click(on_button_clicked)
    display(button)
    return None

def create_google_button():
    js='''console.log('it has begun')
    require.config({
        "shim": {
            "gapi": {
                "exports": "gapi"
            }
        },
        "paths": {
            "gapi": "https://apis.google.com/js/platform"
        }
    })

    require(['gapi'], function (gapi) {
    gapi.load('auth2', function () {
      gapi.auth2.init({
        client_id: '182541249753-uc2ci1ts4lp480bcod4en0j9f0oo0iuh' 
      });
      gapi.signin2.render('g1')
    });
    });'''
    display(Javascript(js))

def get_user_info():
    js='''
    var auth = gapi.auth2.getAuthInstance();
    var user = auth.currentUser.get();
    var info = user.getBasicProfile();
    console.log(info);
    element.append(JSON.stringify(info));
    '''
    display(Javascript(js))
