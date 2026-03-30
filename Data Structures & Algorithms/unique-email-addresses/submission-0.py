class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            parsed_email = ""
            i = 0

            while email[i] not in ["@", "+"]:
                if email[i] == ".":
                    parsed_email += ""
                else:
                    parsed_email += email[i]
                
                i += 1

            if email[i] == "+":
                while email[i] != "@":
                    i += 1

            while i < len(email):
                parsed_email += email[i]
                i += 1
            
            unique_emails.add(parsed_email)

        return len(unique_emails)
