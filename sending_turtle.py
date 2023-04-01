class PostOffice:
    """A Post Office class. Allows users to message each other.

    :ivar int message_id: Incremental id of the last message sent.
    :ivar dict boxes: Users' inboxes.

    :param list usernames: Users for which we should create PO Boxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        """Send a message to a recipient.

        :param str sender: The message sender's username.
        :param str recipient: The message recipient's username.
        :param str message_body: The body of the message.
        :param urgent: The urgency of the message.
        :type urgent: bool, optional
        :return: The message ID, auto incremented number.
        :rtype: int
        :raises KeyError: if the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
        return self.message_id

    def read_inbox(self, username, N=None):
        """
        :param username: str recipient.
        :param N: int number of messages.
        :return: List of the first N messages of a recipient.
        """
        if N is None:
            res = self.boxes[username]
            self.boxes[username] = []
        else:
            res = self.boxes[username][:N]
            self.boxes[username] = self.boxes[username][N:]
        return res

    def search_inbox(self, username, string):
        """
        :param username: str recipient.
        :param string: string to look for in the recipient inbox.
        :return: list of all the messages that contain the string of the recipient inbox.
        """
        return [msg for msg in self.boxes[username] if string in msg['body']]

# Taken from https://github.com/PythonFreeCourse/Notebooks/blob/master/week07/2_Documentation.ipynb
