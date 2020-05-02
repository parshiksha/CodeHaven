console.log('tihs is from editor file');



javaBasicCode =    `
public class MyFirstJavaProgram {

    /* This is my first java program.
     * This will print 'Hello World' as the output
     */
 
    public static void main(String []args) {
       System.out.println("Hello World"); // prints Hello World
    }
 }
`

pythonBasicCode =  `import time
#doing some random shit
def main(x)
    y = x-2
    x = x+1
    print(x)`


CppBasicCode =   `#include <iostream>
using namespace std;

// main() is where program execution begins.
int main() {
   cout << "Hello World"; // prints Hello World
   return 0;
}`

JavaScriptBasicCode = `
function main(x){
    x = x + x *x
    return x
    //do something else

}

`

function chooseLang(){
    var z = document.getElementById("myLang").selectedIndex;
    var y= document.getElementById("myLang").value;
    setupEditor(z);

console.log(z+ y);
}


function update(){
    // var idoc = document.getElementById('iframe').contentWindow.document;
    // idoc.open();
    // idoc.write(editor.getValue());
    // idoc.close();
    console.log("Updating");
}

function setupEditor(x){
    console.log("setup editor working  with value of x is : " + x);


    if(x == 1){
        lagnMode = "ace/mode/java"
        lagnValue = javaBasicCode
    } 
    else if(x == 2){
        lagnMode = "ace/mode/c_cpp"
        lagnValue = CppBasicCode
    }
    else if(x == 3){
        lagnMode = "ace/mode/javascript"
        lagnValue = JavaScriptBasicCode
    } else{
        lagnMode = "ace/mode/python"
        lagnValue = pythonBasicCode
    }

  window.editor = ace.edit("editor");
  editor.setTheme("ace/theme/monokai");
  editor.getSession().setMode(lagnMode);
  editor.setValue(lagnValue,1); //1 = moves cursor to end

editor.getSession().on('change', function() {
  update();
});

editor.focus();


editor.setOptions({
  fontSize: "16pt",
  showLineNumbers: true,
  showGutter: true,
  vScrollBarAlwaysVisible:true,
  enableBasicAutocompletion: false, enableLiveAutocompletion: false
});

editor.setShowPrintMargin(false);
editor.setBehavioursEnabled(false);
}

setupEditor(0)
update();

