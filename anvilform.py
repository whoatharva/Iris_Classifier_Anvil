from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    iris_category = anvil.server.call('predict_iris', 
                                self.sepal_length.text,
                                self.sepal_width.text,
                                self.petal_length.text,
                                self.petal_width.text)
    # If a category is returned set our species 
    if iris_category:
      self.species_label.visible = True
      self.species_label.text = "The species is " + iris_category.capitalize()

  def sepal_length_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def sepal_width_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
