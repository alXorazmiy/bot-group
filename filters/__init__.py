

from loader import dp
from .admins import AdminFilter
from .group_filter import isGroup
from .private_chat import isPrivate


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(isGroup)
    dp.filters_factory.bind(isPrivate)

