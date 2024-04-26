# See:
# http://www.gnu.org/software/make/manual/make.html
# http://linuxlib.ru/prog/make_379_manual.html

.PHONY : build

# This allows us to accept extra arguments
%:
    @:
args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

### Ansible operations
rebuild:
	docker-compose down && docker-compose build && docker-compose up -d && docker-compose logs -f
