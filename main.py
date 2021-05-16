from executor import Executor

"""
mj create
mj create -c -n Vlad -a daily
mj aliases
mj get daily
mj connect daily
mj connect daily -n "Brother"
mj rename daily weekly
mj aliases
mj get weekly
mj alias ca91bd29-874e-46fa-be75-4f6f4cdc8a5f party
mj aliases
mj get party
mj remove party
mj get-config -p
mj get-config
mj set-name "Vlad Lytvynenko"
mj connect weekly
mj set-config example.json
mj get-config -p
mj aliases
mj set-name "Vlad Lytvynenko"
mj connect daily
mj connect daily -n "Oleg Petrov"
"""


if __name__ == '__main__':
    Executor().execute_from_command_line()

# TODO make this installable by pip
# TODO make this executable and add alias with mj? Or just add 
# TODO push to repository
