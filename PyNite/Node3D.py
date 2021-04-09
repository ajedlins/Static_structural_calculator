
class Node3D():
    """
    A class representing a node in a 3D finite element model.
    """
    
    def __init__(self, Name, X, Y, Z):
        """
        Initializes a new node.
        """
        
        self.Name = Name    # A unique name for the node assigned by the user
        self.ID = None      # A unique index number for the node assigned by the program
        
        self.X = X          # Global X coordinate
        self.Y = Y          # Global Y coordinate
        self.Z = Z          # Global Z coordinate
        
        self.NodeLoads = [] # A list of loads applied to the node (Direction, P, case) or (Direction, M, case)
        
        # Initialize the dictionaries of calculated node displacements
        self.DX = {}
        self.DY = {}
        self.DZ = {}
        self.RX = {}
        self.RY = {}
        self.RZ = {}
        
        # Initialize the dictionaries of calculated node reactions
        self.RxnFX = {}
        self.RxnFY = {}
        self.RxnFZ = {}
        self.RxnMX = {}
        self.RxnMY = {}
        self.RxnMZ = {}

        # Initialize all support conditions to 'False'
        self.SupportDX = False
        self.SupportDY = False
        self.SupportDZ = False
        self.SupportRX = False
        self.SupportRY = False
        self.SupportRZ = False

        # Initialize all enforced displacements to 'None'
        self.EnforcedDX = None
        self.EnforcedDY = None
        self.EnforcedDZ = None
        self.EnforcedRX = None
        self.EnforcedRY = None
        self.EnforcedRZ = None
