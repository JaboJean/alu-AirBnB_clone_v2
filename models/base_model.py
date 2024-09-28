class BaseModel:
    """This class defines all common attributes/methods for other classes"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model class."""
        # Define valid keys to expect in kwargs
        valid_keys = {'id', 'created_at', 'updated_at', '__class__'}

        # Check if any key in kwargs is not in valid_keys
        for key in kwargs:
            if key not in valid_keys:
                raise KeyError(f"Unexpected key '{key}' in kwargs")

        # Handle datetime conversion for created_at and updated_at
        if 'updated_at' in kwargs:
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
            )
        if 'created_at' in kwargs:
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
            )

        # Remove __class__ if present in kwargs
        kwargs.pop('__class__', None)

        # Update the object's attributes with kwargs
        self.__dict__.update(kwargs)

        # Generate a new id if not provided
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
