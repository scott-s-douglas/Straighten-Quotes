import sublime
import sublime_plugin

class StraightenQuotesCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        i=0
        for rgn in self.view.find_all("[“”]"):
            self.view.replace(edit, rgn, "\"")
        for rgn in self.view.find_all("[‘’]"):
            self.view.replace(edit, rgn, "\'")

        multicharReplacements = {
        "…":"...",
        "–":"--",
        "—":"---"
        }
        multicharString="["
        for char in multicharReplacements.keys():
            multicharString += char
        multicharString+="]"
        replacement = self.view.find(multicharString,0)
        while replacement.begin() > 0:
            print(replacement)

            self.view.replace(edit,replacement,multicharReplacements[self.view.substr(replacement)])
            replacement = self.view.find(multicharString,0)
