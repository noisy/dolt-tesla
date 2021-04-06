class DjangoRouter:
    django_apps_labels = {'admin', 'auth', 'contenttypes', 'sessions'}

    def get_db(self, label):
        print("app_label: ", label)
        if label in self.django_apps_labels:
            print("DB:default")
            return 'default'

        print("DB:dolt")
        return 'dolt'

    def db_for_read(self, model, **hints):
        return self.get_db(model._meta.app_label)

    def db_for_write(self, model, **hints):
        return self.get_db(model._meta.app_label)

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.django_apps_labels and db == 'default':
            return True
        if app_label in 'data' and db == 'dolt':
            return True
        return False

