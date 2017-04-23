class MicrochipDestroyed(Exception):
    """
    This is raised when there is a microchip on a floor without its
    corresponding generator, but with a generator of a different type.
    """
    pass
