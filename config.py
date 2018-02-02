class Config(object):
  """ Base config class."""
  def __init__(self):
    pass

class ProdConfig(Config):
  """Production config class."""
  pass

class DevConfig(Config):
  """ Development config class."""
  # Open the DEBUG
  DEBUG = True

